---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 5
---

# Ifosfamide
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

# Ifosfamide：從烷化劑化療到女性乳癌 (Female Breast Carcinoma)

## 一句話總結

Ifosfamide 是一種烷化劑類的細胞毒性化療藥物，香港已有 4 張許可證，但許可證資料未載明原適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前有 **7 個相關臨床試驗登記**，多為 Phase 1/2 或未知狀態，**沒有文獻**支持，尚無已完成的隨機對照試驗結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L2（Evidence Pack 暫定，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

**證據等級說明：** 依判定規則，L2 需要「已完成的 Phase 2/3 RCT」。目前登記的 Phase 3 與 Phase 2 試驗狀態多為「未知」，且都沒有結果資料，也沒有已完成的 Phase 2/3 RCT。L2 是沿用 Evidence Pack 的暫定判定，實際證據強度應視為偏弱。

## 為什麼這個預測合理？

Ifosfamide 是 oxazaphosphorine 類烷化劑前驅藥。它在肝臟被活化為 isophosphoramide mustard，與 DNA 形成交叉鏈結，誘發快速增生細胞凋亡。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自一般藥理知識。

乳癌對細胞毒性化療藥物有一定反應性，因此烷化劑用於乳癌在生物學上說得通。TxGNN 分數很高（99.91%），但這只是模型預測，不能取代臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | 未知 | 42 | Docetaxel + Ifosfamide 作為轉移性乳癌第一線治療，無結果資料 |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | 未知 | 637 | Paclitaxel + Carboplatin 對比 Ifosfamide + Paclitaxel，用於子宮／輸卵管／腹膜／卵巢癌肉瘤，無結果資料 |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | 未知 | 未提供 | 多週期高劑量化療對比常規劑量化療，用於轉移性乳癌，Ifosfamide 的角色不明 |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 終止 | 未提供 | TIME 方案（Topotecan、Ifosfamide/Mesna、Etoposide）加自體幹細胞救援，用於轉移性乳癌 |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | 完成 | 33 | 含 Ifosfamide 的序列高劑量化療加自體幹細胞支持，用於晚期癌症，無法單獨評估 Ifosfamide |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | 終止 | 12 | Samarium-153 併雙次自體骨髓移植，用於第 IV 期乳癌，Ifosfamide 至多是背景藥物 |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | 終止 | 7 | 幹細胞移植後活化 T 細胞治療第 IV 期乳癌，Ifosfamide 至多是背景藥物 |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | 無分期 | 未知 | 35 | 以病人來源類器官藥物篩選挑選化療，用於難治性實體腫瘤，Ifosfamide 只是候選藥物之一 |

**注意：** NCT00954174 的適應症是子宮、輸卵管、腹膜或卵巢癌肉瘤，**不是乳癌**。Evidence Pack 的相關性評語稱它直接測試乳癌，與試驗標題不符，因此不應把它當作乳癌的直接證據。
真正直接針對乳癌、且以 Ifosfamide 組合為測試對象的只有 NCT00026078（Phase 2，狀態未知，無結果）。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64831 | IFO-CELL N 1000 SOLUTION FOR INFUSION 1000MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-61271 | IFOSFAMIDE POWDER FOR SOLUTION FOR INFUSION 1G (QILU HAINAN) | JINDUN PHARMA (H.K.) LIMITED |
| HK-01322 | HOLOXAN INJ IV | BAXTER HEALTHCARE LIMITED |
| HK-50758 | ISOXAN FOR INJ 1000MG | HEALTHCARE PHARMASCIENCE LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑，oxazaphosphorine 類） |
| 骨髓抑制風險 | 中至高（依劑量與併用藥物而異，Evidence Pack 無 toxicity 資料，此為依藥物類別的判斷） |
| 致吐性分級 | 中至高（依劑量而異，依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能、尿液檢查（血尿）、電解質、神經系統狀態 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；臨床常搭配 mesna 預防出血性膀胱炎 |

上表為依藥物類別的一般判斷，詳細警語請參考原廠仿單。

## 安全性考量

安全性資訊請參考原廠仿單。

另有一點需注意：烷化劑（包括 Ifosfamide）與治療相關的骨髓增生異常症候群／急性骨髓性白血病有關。TxGNN 對 Ifosfamide 的其他預測（未分類骨髓增生異常症候群、5q 缺失、兒童難治性血球低下、先天性環狀鐵粒幼細胞貧血）都沒有支持證據。
其中前三項可能反映的是藥物不良結果的關聯，而非治療關係。這些預測建議一律不推進，先以 Hold 處理。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳癌適應症在機轉上合理，但直接證據薄弱：只有 1 個直接相關的 Phase 2 試驗（NCT00026078），狀態未知、無結果，且沒有任何文獻。
- 香港許可證的適應症與仿單警語資料都缺失，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症。
- 取得 NCT00026078 與 NCT00954174 的結果或發表文獻，確認療效與安全性。
- 補充 DrugBank 的作用機轉資料，並與乳癌現行標準治療比較 Ifosfamide 的定位。
- 檢索並評估 Ifosfamide 用於乳癌的文獻（目前為零）。

*本報告結果僅供研究參考，不構成醫療建議。預測適應症需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

