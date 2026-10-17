---
layout: default
title: Bedaquiline
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bedaquiline：預測新適應症為非活動性結核病 (Inactive Tuberculosis)（證據等級 L5）。原適應症：肺結核、多重抗藥性結核病"
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
---

# Bedaquiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Bedaquiline：從肺結核與多重抗藥性結核病到非活動性結核病（潛伏性結核感染預防）

## 一句話總結

Bedaquiline 是一種抗結核藥物，原本用於肺結核及多重抗藥性結核病（MDR-TB）的治療。
TxGNN 模型預測它可能對**非活動性結核病 (Inactive Tuberculosis)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**支持這個方向，但尚無已完成的 RCT 結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺結核、多重抗藥性結核病（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 非活動性結核病 (Inactive Tuberculosis) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L2（有 Phase 2/3 試驗，但尚未完成、無結果） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：預測分數前幾名的疾病（牛結核、結核性腹水、非活動性結核病、禽結核、結核瘤）分數幾乎相同。本報告以 BREACH-TB 試驗所支持、證據最充分的「非活動性結核病」為主軸。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。不過根據文獻，Bedaquiline 抑制結核分枝桿菌的 F-ATP 合成酶，破壞細菌能量代謝。文獻也指出它對休眠或持續存活型細菌有作用，這與潛伏性感染的治療與預防相關。

非活動性（潛伏性）結核與已核准的肺結核、MDR-TB 由同一種病原體引起。現行潛伏性結核的預防方案療程長、完成率不一，因此以 Bedaquiline 縮短療程（4 週）是合理的研究方向。

需要注意：目前支持預防用途的主要證據是進行中的 BREACH-TB 試驗，尚無完成的 RCT 數據證實療效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | 招募中 | 2530 | BREACH-TB：比較 4 週 Bedaquiline 與標準方案，預防 HIV 感染者及高風險接觸者發生結核病的非劣性試驗（尚無結果） |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | 進行中（不再招募） | 288 | CRUSH-TB：含 Bedaquiline 的 17 週短程方案 vs 標準 6 個月方案，用於肺結核（針對活動性疾病） |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | 尚未招募 | 60 | 哺乳婦女服用抗結核藥（含 Bedaquiline）後的血漿與乳汁藥物動力學（無療效資料） |

---

## 文獻證據

文獻皆為綜述，沒有 RCT；以下列出與 Bedaquiline 及潛伏性/非活動性結核最相關的 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Pat Anti-Infect Drug Discov | Bedaquiline 有望縮短並改善抗結核療程 |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | 結核分枝桿菌 F-ATP 合成酶抑制劑與標的 |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Review | Infect Disord Drug Targets | Bedaquiline 可針對持續存活或潛伏型細菌；探討新型遞送系統 |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | Zhejiang Da Xue Xue Bao Yi Xue Ban | 潛伏性結核感染的診斷與治療進展 |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | 結核病呈現疾病光譜，亞臨床結核對傳播影響大 |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clin Pharmacol Ther | 結核病治療總覽，涵蓋潛伏性與活動性結核 |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | Lancet Infect Dis | 新藥、短程療法與宿主導向治療的進展 |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | Review | Int J Mycobacteriol | 針對非複製型結核菌的藥物策略 |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Review | Pathogens | 兒童抗藥性結核的管理與預防，含 Bedaquiline 等新藥 |
| [36105740](https://pubmed.ncbi.nlm.nih.gov/36105740/) | 2022 | Review | Curr Res Pharmacol Drug Discov | Pretomanid 更新；Bedaquiline 已移至 A 組藥物 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64766 | SIRTURO TABLETS 100MG | — | 未提供 |

製造商：Johnson & Johnson (Hong Kong) Ltd.，狀態有效。

---

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分重要者。
  - 重大（Major）：Dexamethasone、Clarithromycin、Dolasetron、Palonosetron、Picosulfuric acid、Sodium sulfate、Polyethylene glycol（含電解質）
  - 中度（Moderate）：Acarbose、Famotidine、Doxycycline、Minocycline、Tetracycline、Pioglitazone、Loperamide、Bupropion、Naltrexone 等
- **其他提醒**：抗結核藥物有肝毒性風險，方案設計時需留意（相關病例報告見其他預測適應症的文獻）。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 非活動性結核病是排名中唯一有 Phase 2/3 臨床試驗直接支持的預測，機轉合理，且藥物已在香港上市。但試驗尚未完成，無療效結果，故需設防護條件推進。
- 其他高分預測（牛結核、結核性腹水、禽結核、結核瘤、皮膚結核）證據僅為體外研究或病例報告，建議暫緩（Hold）。陰道念珠菌病、肝片吸蟲症、尿素循環障礙、食道念珠菌病則缺乏機轉依據，高分可能是圖譜相似性造成的假象。

**若要推進需要：**
- 追蹤 BREACH-TB（NCT06568484）的結果（預計 2027 年 9 月完成）
- 取得香港仿單的警語、禁忌症及核准適應症
- 補充詳細作用機轉資料
- 制定預防用途的安全性監測計畫（肝功能、QT 間期、藥物交互作用管理）
- 評估特殊族群（HIV 感染者、哺乳婦女、兒童）的使用條件
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

