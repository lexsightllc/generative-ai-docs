/**
 * Copyright 2023 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from 'react';
import { Card } from '@mui/material';

export default function PromptCard(props) {
  const { children, color, onClick } = props;
  return (
    <Card
      sx={{
        borderRadius: '5px',
        boxShadow: '0px 2px 5px rgba(0, 0, 0, 0.06)',
        fontSize: '1rem',
        fontWeight: 400,
        color: color,
        padding: '1.15rem',
        overflow: 'hidden',
        position: 'relative',
        display: 'inline',
        textAlign: 'right',
      }}
      onClick={onClick}
    >
      <span>{children}</span>
    </Card>
  );
}
