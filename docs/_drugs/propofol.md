---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 739
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Propofol：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：目前香港許可證資料未載明核准適應症"
monitor_inn: "PROPOFOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol：從麻醉與鎮靜到偏頭痛

## 一句話總結

Propofol 是常用的靜脈麻醉與鎮靜藥物。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多項隨機對照試驗與系統性回顧。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前香港許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L1（依資料編譯結果；詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：臨床試驗中僅 1 個為已完成的 Phase 2/3 試驗，嚴格依本報告的等級規則較接近 L2；但另有多項已發表的 RCT 與系統性回顧，資料編譯結果將其評為 L1。判讀時請留意此差異。

## 為什麼這個預測合理？

Propofol 是 GABA-A 受體的正向別構調節劑。增強 GABA 抑制作用，可能降低三叉神經血管系統的痛覺訊號傳遞，以及大腦皮質的過度興奮。前臨床研究也顯示，propofol hemisuccinate 能抑制皮質擴散性抑制 (cortical spreading depression)，而這被認為是偏頭痛先兆的神經基礎。

在臨床上，亞麻醉劑量的 propofol 已被用於急診中難治型急性偏頭痛，作為標準治療失效後的選項。因此這個預測在機轉與臨床使用經驗上都有合理依據。

需注意：本次編譯的資料缺乏完整的作用機轉紀錄，上述機轉說明來自預測分析的推論。此外，propofol 有鎮靜與呼吸抑制風險，只適合在有監測的環境（如急診）使用。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | 完成 | 74 | 低劑量 propofol 用於兒童急診偏頭痛的急性緩解治療；直接針對本適應症，但僅限兒童族群 |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | 完成 | 40 | 低劑量 propofol 輸注用於兒童偏頭痛，評估療效、安全劑量與作用持續時間 |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | 提前終止 | 12 | 低劑量 propofol 用於急診嚴重難治型偏頭痛；因收案過少，可解讀的療效資料有限 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | 低劑量 propofol 用於兒童偏頭痛的前瞻性隨機對照試驗 |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT（前導） | Emerg Med Australas | 急診以鎮靜劑量 propofol 與標準治療比較，作為偏頭痛初始處置 |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol 合併 granisetron 與合併 metoclopramide 的症狀控制比較 |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Sumatriptan 加 propofol 與單用 sumatriptan 在急性偏頭痛的療效比較 |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | 系統性回顧 | Acad Emerg Med | 評估 propofol 用於急診急性偏頭痛的安全性與療效；指出現有證據有限 |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | 系統性回顧 | Headache | 兒童偏頭痛急診急性治療的質性系統性回顧 |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | 系統性回顧／網絡分析 | Headache | 比較各種注射藥物降低急性偏頭痛復發的效果 |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | 指引 | Headache | 美國頭痛學會 2025 年急診成人偏頭痛注射藥物治療指引更新 |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Review | Expert Rev Neurother | 說明 propofol 用於超難治型偏頭痛的藥物特性 |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | 臨床報告 | Headache | 門診頭痛中心使用靜脈 propofol 治療難治型偏頭痛的經驗 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27322 | DIPRIVAN INJ 1% | 注射劑 | 資料未載明 |
| HK-66287 | PROPOFOL-LIPURO EMULSION FOR INJECTION/INFUSION 500MG/50ML | 注射／輸注用乳劑 | 資料未載明 |
| HK-55671 | FRESOFOL INJ 1% MCT/LCT | 注射劑 | 資料未載明 |
| HK-66286 | PROPOFOL-LIPURO EMULSION FOR INJECTION/INFUSION 200MG/20ML | 注射／輸注用乳劑 | 資料未載明 |
| HK-49677 | PROPOFOL-LIPURO INJ 1% | 注射劑 | 資料未載明 |

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物－疾病關聯資料，並非仿單原文）：癲癇、低血壓、呼吸衰竭、顱內動脈硬化、遺傳性脂質代謝異常、家族性高脂血症。
- **藥物交互作用**：共查得 100 筆，以下列出部分例子。
  - 中度：famotidine、clarithromycin、levofloxacin、ondansetron、granisetron、dolasetron、cisapride、morphine、loperamide，以及多種瀉劑（bisacodyl、lactulose 等）
  - 輕度：metronidazole
- **使用情境提醒**：用於偏頭痛時有鎮靜與呼吸抑制風險，須在有監測的環境（如急診）中使用。
- **其他可預期的風險**：Prinzmetal 心絞痛的文獻顯示，麻醉誘導期間曾出現冠狀動脈痙攣的案例，應列為心血管風險的警示。

仿單的警語與禁忌症全文尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有已完成的 Phase 2/3 試驗、多項 RCT 與系統性回顧，加上 GABA-A 機轉與前臨床證據，支持 propofol 用於急診難治型偏頭痛。
- 但多數試驗為小型或兒童研究，且有鎮靜、呼吸抑制與心血管風險，只適合在受監測的環境下作為二線選項。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症全文，完成安全性篩選
- 取得 DrugBank 的作用機轉資料，補強機轉分析
- 針對成人急診族群的較大型 RCT 結果進行確認，並釐清兒童與成人的證據差異
- 制定使用場域、劑量、監測與人員資格的規範

## 其他預測適應症（供參考）

| 預測適應症 | 分數 | 證據等級 | 建議 | 說明 |
|-----------|------|---------|------|------|
| 伴腦幹先兆的偏頭痛 | 99.58% | L4 | Research Question | 前臨床資料顯示可抑制皮質擴散性抑制，但無針對此亞型的試驗，且腦幹症狀與意識和呼吸改變重疊，安全疑慮較高 |
| Prinzmetal 心絞痛 | 99.23% | L4 | Hold | 現有文獻是麻醉中誘發冠狀動脈痙攣的案例，屬安全警訊，而非療效證據 |
| 腎因性抗利尿激素不適當分泌症候群 | 99.20% | L5 | Hold | 無試驗、無文獻，也無合理機轉，僅為模型預測 |
| Tourette 症候群 | 99.03% | L4 | Hold | 僅有深部腦刺激手術中鎮靜的神經生理研究，未顯示對抽動症狀有療效 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

