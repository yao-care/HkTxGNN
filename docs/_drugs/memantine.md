---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 561
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Memantine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：許可證資料未載明"
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine：從 阿茲海默症相關適應症（香港許可證未載明）到 偏頭痛 (Migraine Disorder)

## 一句話總結

Memantine 是 NMDA 受體拮抗劑，在香港已有 8 張有效許可證。這份資料未載明其核准適應症文字。
TxGNN 模型預測排名最高的新適應症是肺高壓（分數最高，但證據僅為模型預測）。證據最完整的是**偏頭痛 (Migraine Disorder)**，目前有 **1 個 Phase 3 臨床試驗**和 **約 20 篇文獻**，但整體證據仍屬有限。

> 說明：肺高壓排名第 1，但其文獻並未支持臨床關聯。因此本報告以證據最完整的偏頭痛為主軸，並在下方列出各預測的比較。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder)（TxGNN 排名第 2；排名第 1 為肺高壓，但缺乏證據） |
| TxGNN 預測分數 | 99.52%（肺高壓為 99.54%） |
| 證據等級 | L1（僅憑 1 個小型 Phase 3 試驗，須謹慎解讀） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails（偏頭痛）；肺高壓與脊柱後側彎性心臟病為 Hold |

### 各預測適應症比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 肺高壓 (Pulmonary Hypertension) | 99.54% | L5 | Hold |
| 2 | 偏頭痛 (Migraine Disorder) | 99.52% | L1（宜保守看待） | 研究性問題 |
| 3 | 脊柱後側彎性心臟病 (Kyphoscoliotic Heart Disease) | 99.43% | L5 | Hold |
| 4 | 腦幹型先兆偏頭痛 (Migraine with Brainstem Aura) | 99.41% | L4 | 研究性問題 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠 MOA 欄位未收錄）。就已知藥理，Memantine 是非競爭性 NMDA 型麩胺酸受體拮抗劑。

偏頭痛的病理生理與麩胺酸訊號有關：皮質擴散性抑制 (cortical spreading depression)、中樞敏感化與三叉神經血管系統活化，都涉及 NMDA 受體。數篇回顧指出，偏頭痛患者腦中麩胺酸濃度偏高，且相關基因與麩胺酸訊號有關。因此，抑制 NMDA 受體以降低神經元過度興奮，在機轉上說得通。

不過，文獻也以「前景大但證據少 (big promise but little evidence)」描述 Memantine 用於偏頭痛的現況，需更大型的安慰劑對照試驗確認。腦幹型先兆偏頭痛的推論則更間接，主要由一般偏頭痛的證據外推。

肺高壓方面，雖有 NMDA 受體參與肺血管張力的前臨床推測，但檢索到的文獻並未提供臨床支持。唯一相關的新資料是 Memantine 硝酸鹽衍生物 MN-08 的 Phase 1 研究，屬於不同化合物，不能直接類推。

---

## 臨床試驗證據

**偏頭痛**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | 完成 | 33 | Memantine 對比 Valproate 用於陣發性偏頭痛預防；樣本小，結果數據未提供 |

肺高壓、脊柱後側彎性心臟病、腦幹型先兆偏頭痛：目前無相關臨床試驗登記。

---

## 文獻證據

**偏頭痛（優先列出系統性回顧、統合分析與 RCT 相關文獻）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | 統合分析（RCT） | Clin Neuropharmacol | 比較 Memantine 與安慰劑用於偏頭痛的療效，過往結果仍有爭議 |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | 系統性回顧 | Headache | 評估 Memantine 預防陣發性偏頭痛的療效與安全性 |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | 系統性回顧 | Ann Pharmacother | 回顧 Memantine 預防原發性頭痛的資料 |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | 網絡統合分析 | Front Pharmacol | 比較成人偏頭痛口服預防藥物的療效與安全性 |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedeberg's Arch Pharmacol | 整理 Memantine 與 Ketamine 作為抗偏頭痛藥物的證據 |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | 評論 | Headache | 指出 Memantine 用於偏頭痛前景大但證據少 |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | 回溯性研究 | J Headache Pain | 60 例患者使用 Memantine 預防偏頭痛的回溯性分析 |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | 麩胺酸及其受體是偏頭痛的治療標的 |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | 臨床指引 | Ann Intern Med | 2023 年 VA/DoD 頭痛處置指引 |
| [34048395](https://pubmed.ncbi.nlm.nih.gov/34048395/) | 2021 | Review | Continuum | 偏頭痛預防性治療概述 |

**腦幹型先兆偏頭痛（間接證據）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT（無先兆偏頭痛，間接） | Headache | 雙盲安慰劑對照試驗，評估 Memantine 預防無先兆偏頭痛 |
| [36983158](https://pubmed.ncbi.nlm.nih.gov/36983158/) | 2023 | Review（前臨床/機轉） | J Clin Med | 周邊 NMDAR 作為偏頭痛治療新策略 |

**肺高壓**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | 前臨床 | Theranostics | NMDA 受體活化調控胰島素敏感性與脂質代謝，與肺高壓僅間接相關 |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/安全性（不同化合物 MN-08） | Clin Drug Investig | Memantine 硝酸鹽衍生物在健康中國受試者的安全性與藥動學 |

脊柱後側彎性心臟病：目前無相關文獻。

---

## 香港上市資訊

香港共有 8 張有效單方許可證，核准適應症文字在這份資料中皆未載明。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51749 | EBIXA TAB 10MG | 錠劑 | 未載明 |
| HK-58231 | EBIXA TAB 20MG | 錠劑 | 未載明 |
| HK-62748 | MEMANTINE ACTAVIS FILM-COATED TABLETS 10MG | 膜衣錠 | 未載明 |
| HK-63963 | MEMANTINE SANDOZ TABLET 10MG | 錠劑 | 未載明 |
| HK-62744 | ALBIX TABLETS 10MG | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**：肝病、膽囊疾病、腎功能不全（此為知識圖譜的藥物-疾病禁忌關聯，並非仿單內容，需對照仿單確認）。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例：
  - 中度：抗膽鹼藥物類，如 Hyoscyamine、Atropine、Glycopyrronium、Clidinium、Dicyclomine、Scopolamine、Trospium 等
  - 輕度：Ranitidine、Metformin、Cimetidine、Potassium citrate
  - 等級未明：Glimepiride、Doxycycline、Lansoprazole、Loperamide、Famotidine、阿斯匹靈

仿單中的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（偏頭痛）；肺高壓與脊柱後側彎性心臟病維持 Hold**

**理由：**
- 偏頭痛有機轉合理性、1 個已完成的 Phase 3 試驗，以及多篇系統性回顧與統合分析。但該試驗僅 33 人且結果未提供，L1 等級須保守解讀，現階段屬於研究性問題。
- 肺高壓雖然 TxGNN 分數最高，但僅為模型預測，檢索文獻並未支持臨床關聯，故不建議推進。

**若要推進需要：**
- 取得香港仿單的警語與禁忌症，完成安全性篩查（此為阻斷性資料缺口）
- 取得香港許可證核准適應症，以確認原適應症
- 補充詳細作用機轉（MOA）資料
- 取得 NCT04698525 的結果，並分析已發表統合分析的效應量與異質性
- 規劃更大型的安慰劑對照偏頭痛預防試驗
- 肺高壓方面，需先有機轉與前臨床證據，再評估是否值得探索
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

