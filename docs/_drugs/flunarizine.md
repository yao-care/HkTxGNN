---
layout: default
title: Flunarizine
parent: 高證據等級 (L1-L2)
nav_order: 323
evidence_level: L1
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Flunarizine：從眩暈到偏頭痛

## 一句話總結

Flunarizine 是一種選擇性鈣離子通道阻斷劑，在多國已核准用於眩暈（前庭疾病）與偏頭痛的預防治療，但在香港目前尚無正式上市許可。TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，此預測與全球廣泛的臨床實證高度吻合。目前有 **19 個臨床試驗**和 **20 篇文獻**直接支持 Flunarizine 在偏頭痛領域的療效，美國、加拿大及歐洲三大神經學會指引均已引用其臨床證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 眩暈（前庭系統疾病）；多國核准偏頭痛預防 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.12% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Flunarizine 是一種選擇性 T/L 型鈣離子通道阻斷劑，兼具抗組織胺與多巴胺 D2 受體拮抗特性。其預防偏頭痛的機轉已被充分研究：① 抑制皮質擴散性抑制（Cortical Spreading Depression, CSD）——偏頭痛先兆的關鍵神經電生理事件；② 降低三叉神經血管系統的異常放電敏感度；③ 阻斷顱內血管的鈣依賴性收縮，穩定血管張力；④ 輕度 5-HT2 拮抗，調節疼痛傳導路徑。

偏頭痛與鈣離子通道功能異常有密切關聯。家族性偏癱型偏頭痛（Familial Hemiplegic Migraine）的基因研究已確認 CACNA1A（P/Q 型鈣通道）突變為重要致病因子，進一步支持鈣離子阻斷劑在偏頭痛的機轉合理性。Flunarizine 透過阻斷鈣離子內流，直接干預偏頭痛核心病理機轉，這正是其 TxGNN 高評分（0.991）的機轉基礎——知識圖譜中藥物節點與偏頭痛節點之間的連結密度，精確反映了這份成熟的生物學依據。

Flunarizine 目前在歐洲、日本、韓國、印度及部分拉丁美洲國家均已核准用於偏頭痛預防。歐洲頭痛聯合會（EHF）於 2023 年發表其偏頭痛預防療效 Meta 分析（PMID 37723437），加拿大頭痛學會及美國神經病學學會（AAN）指引亦均列出其臨床數據。香港雖尚未正式核准上市，但國際證據體系已達 L1 等級，TxGNN 預測與現有臨床實踐高度一致。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | 已完成 | 120 | 三臂比較：枕大神經阻斷 vs Topiramate vs **Flunarizine** 用於發作性偏頭痛預防，以 VAS 評分與發作頻率降低為主要終點，最具直接比較價值的已完成試驗 |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | 已完成 | 62 | **Flunarizine** 10mg/day vs Topiramate 50mg/day 用於慢性偏頭痛預防的直接比較 RCT |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | 未知 | 84 | **Flunarizine** vs Amitriptyline 偏頭痛預防性治療比較，以急性發作頻率與 VAS 疼痛分數為主要終點（巴基斯坦三級醫院） |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | 招募中 | 44 | **Flunarizine** vs Propranolol 用於 8–15 歲小兒偏頭痛，以 PedMIDAS 評分為主要終點 |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | 尚未招募 | 460 | PREMI 研究：四臂務實臨床試驗，比較 Amitriptyline、**Flunarizine**、Topiramate、Propranolol 用於初級醫療偏頭痛第一線預防 |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | 已完成 | 60 | Alpha-lipoic acid 附加於 **Flunarizine** 背景治療的青少年偏頭痛預防 RCT，**Flunarizine** 作為標準對照基礎治療 |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | 已完成 | 75 | **Flunarizine** + Topiramate 藥動學交互作用研究（偏頭痛背景），評估聯合治療安全性，確認偏頭痛場景中的臨床使用現況 |
| [NCT04702971](https://clinicaltrials.gov/study/NCT04702971) | Phase 4 | 未知 | 600 | 偏頭痛疼痛敏感度多模態腦幹神經影像學研究，探索偏頭痛神經生理機轉，受試者族群包含標準藥物治療組 |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | N/A | 尚未招募 | 2000 | CGRP 靶向藥物用於前庭偏頭痛（Vestibular Migraine）的中國真實世界研究，**Flunarizine** 為標準預防治療對照組之一 |
| [NCT00740259](https://clinicaltrials.gov/study/NCT00740259) | Phase 4 | 已完成 | 70 | **Flunarizine** vs Haloperidol 的 Phase 4 雙盲 RCT，測試其 D2 受體拮抗機轉，佐證藥物多重藥理特性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic Review & Meta-Analysis | J Assoc Physicians India | 比較 Amitriptyline vs Propranolol 和 **Flunarizine** 偏頭痛預防療效與安全性，最新 Meta 分析 |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | 小兒偏頭痛預防性藥物網絡 Meta 分析，涵蓋 **Flunarizine** 相對療效與安全性比較 |
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Systematic Review & Meta-Analysis | J Headache Pain | 歐洲頭痛聯合會（EHF）**Flunarizine** 偏頭痛預防系統性回顧與 Meta 分析，評定其一線/二線地位 |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic Review + Economic Modelling | Health Technology Assessment | 慢性偏頭痛預防藥物（含 **Flunarizine**）系統性回顧與衛生技術評估，比較 CGRP 單抗與傳統藥物效益 |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Clinical Practice Guideline (AAN) | Neurology | 美國神經病學學會小兒偏頭痛預防藥物治療指引（更新版），評估 **Flunarizine** 在小兒族群的證據 |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Clinical Practice Guideline (Canadian) | Can J Neurol Sci | 加拿大頭痛學會偏頭痛預防指引，**Flunarizine** 列為發作性偏頭痛推薦預防藥物 |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurol Scand | **Flunarizine** 聯合經皮眶上神經刺激（tSNS）vs 單獨治療偏頭痛預防 RCT，顯示聯合療法療效優於單一治療 |
| [35791513](https://pubmed.ncbi.nlm.nih.gov/35791513/) | 2022 | Clinical Study | Brain and Behavior | **Flunarizine** 聯合 Duloxetine 治療慢性偏頭痛合併抑鬱焦慮的臨床療效研究，探討共病情境下的組合策略 |
| [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/) | 1997 | Prospective Multi-centre Study | Pharmacy World Sci | **Flunarizine** 用於偏頭痛預防與眩暈治療的大型上市後研究（n=884），系統評估抑鬱症與錐體外症候群風險 |
| [39324692](https://pubmed.ncbi.nlm.nih.gov/39324692/) | 2024 | Narrative Review | Expert Rev Neurother | 前庭偏頭痛治療選項最新概述，分析 **Flunarizine** 在前庭偏頭痛次族群的臨床地位 |

---

## 香港上市資訊

根據現有資料，Flunarizine 在香港**目前未有正式上市許可**，無登記藥品許可證。

> ⚠️ **注意**：Flunarizine（商品名 Sibelium®，Janssen）在日本、韓國、歐洲各國及東南亞多國均有核准上市，用於眩暈（前庭系統疾病）與偏頭痛預防。香港未上市不代表臨床無效，但在香港使用需特別關注藥物取得管道（如特別進口申請）及相關法規合規問題。

---

## 安全性考量

安全性詳細資訊請參考原廠仿單。

根據現有臨床文獻所揭示的已知安全性輪廓，Flunarizine 長期使用需特別注意以下事項：
- **嗜睡**：常見，尤其治療初期
- **體重增加**：長期使用可觀察到
- **錐體外症候群**（Extrapyramidal symptoms）：與其 D2 受體拮抗活性相關，長期使用需監測（NCT00740259 研究設計即基於此機轉）
- **抑鬱情緒**：上市後研究（PMID 9443168，n=884）系統監測此風險
- **哺乳期婦女**：使用需特別謹慎，建議參考哺乳安全評估（PMID 25217187）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Flunarizine 用於偏頭痛預防已具備充分的 L1 等級臨床證據，包含多個已完成的比較性 RCT、三項主要國際頭痛學會指引（AAN、加拿大、EHF）以及最新系統性回顧 Meta 分析；TxGNN 評分 99.12% 準確反映其高度機轉相關性，預測具有高可信度。然而，香港目前無正式上市許可，安全性仿單資料亦尚待補全，需在監管框架明確後方可推進。

**若要推進需要：**
- 釐清香港法規路徑（特別進口申請 vs 正式新藥上市申請）
- 取得原廠仿單全文（Sibelium® SmPC），完成安全性初評，解決 DG001 阻塞性資料缺口
- 補充正式作用機轉文獻引用（DG002），鞏固機轉關聯性分析
- 建立長期使用的錐體外症候群與抑鬱症狀監測計畫（建議定期神經學評估）
- 參考 EHF Meta 分析（PMID 37723437）確立 Flunarizine 相較 Topiramate、Propranolol 的臨床定位與選擇依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

