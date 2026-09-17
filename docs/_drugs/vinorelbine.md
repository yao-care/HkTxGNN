---
layout: default
title: Vinorelbine
parent: 高證據等級 (L1-L2)
nav_order: 797
evidence_level: L2
indication_count: 5
---

# Vinorelbine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Vinorelbine：從未載明原適應症到尤文氏肉瘤 (Ewing Sarcoma)

## 一句話總結

Evidence Pack 未提供 Vinorelbine 在香港的核准適應症紀錄（該藥物目前未在香港上市），原始適應症資料存在缺口。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing Sarcoma)** 有效，
目前有 **4 個臨床試驗**和 **5 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（藥物未在香港上市，且原始核准適應症未提供） |
| 預測新適應症 | 尤文氏肉瘤 (Ewing Sarcoma) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 DrugBank 未提供 Vinorelbine 正式的作用機轉 (MOA) 摘要資料，此為已知資料缺口。根據佐證資料中的機轉推論，Vinorelbine 為長春花生物鹼 (Vinca alkaloid) 類微管抑制劑，透過抑制微管聚合阻斷細胞有絲分裂，屬於傳統細胞毒性化療藥物之作用模式。

由於 Evidence Pack 未提供 Vinorelbine 在香港的核准適應症紀錄，無法直接比較原適應症與尤文氏肉瘤之間的臨床關聯性。然而根據其藥理分類，Vinorelbine 屬於廣泛用於實體腫瘤化療之細胞毒性藥物，其抗有絲分裂機轉理論上可延伸應用於其他高增殖惡性腫瘤。

尤文氏肉瘤屬於小圓細胞肉瘤，具有高增殖特性，對微管抑制劑理論上敏感。多項兒童腫瘤 Phase 2 單臂試驗已直接測試 Vinorelbine（單獨或併用 Cyclophosphamide）於復發/難治性肉瘤族群（含 Ewing sarcoma），顯示此為已知化療機轉之延伸應用，而非全新機轉假說。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | 已完成 | 50 | 評估 Vinorelbine（Navelbine）於兒童復發或難治性惡性腫瘤之療效 |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | 狀態不明 | 210 | 評估 Vinorelbine 併用 Cyclophosphamide 於難治性/復發性腫瘤（含橫紋肌肉瘤、尤文氏肉瘤、骨肉瘤、神經母細胞瘤、髓母細胞瘤）之抗腫瘤活性 |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | 招募中 | 105 | 兒童及年輕成人多癌別 master protocol（CAMPFIRE），提供共同研究架構以提升試驗效率，新藥物將陸續納入不同癌別子研究 |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | 不適用（觀察性） | 進行中（不再招募） | 100 | 前瞻性多中心世代研究，評估風險分層治療策略於中國兒童尤文氏肉瘤患者之療效與安全性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 Trial | European journal of cancer | 評估 Vinorelbine 併用低劑量口服 Cyclophosphamide 於兒童及年輕成人復發/難治性實體腫瘤之療效、安全性與藥物動力學，對橫紋肌肉瘤顯示良好耐受性與療效 |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 Trial | Cancer | 評估 Vinorelbine 於先前已治療之兒童晚期肉瘤之活性，顯示對橫紋肌肉瘤有效 |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in pharmacology | 軟組織肉瘤化療藥物之系統性回顧，探討不同組織型態選擇適當化療藥物之挑戰 |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | International journal of cancer | PLK1 抑制劑 BI 6727 與微管抑制藥物（含 Vinorelbine）於尤文氏肉瘤細胞中協同誘導細胞凋亡 |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case Report | BMC urology | 腎臟原發性尤文氏肉瘤/外周原始神經外胚層腫瘤（EWS/pPNET）罕見病例報告與文獻回顧，強調診斷困難且影像表現無特異性 |

---

## 香港上市資訊

此藥物目前**未在香港取得任何藥品許可證**（許可證數：0），無上市紀錄可供比對核准適應症。

---

## 細胞毒性

Vinorelbine 屬於長春花生物鹼 (Vinca alkaloid) 類細胞毒性化療藥物，符合傳統抗腫瘤藥物分類。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Vinca alkaloid 微管抑制劑類） |
| 骨髓抑制風險 | 高（Vinca alkaloid 類藥物常見顯著嗜中性白血球減少症，通常為劑量限制性毒性；具體毒性數據缺失，此為藥理類別一般性推論） |
| 致吐性分級 | 低至中度 |
| 監測項目 | 全血球計數 (CBC，含白血球分類)、肝功能、周邊神經學評估（Vinca alkaloid 相關神經毒性） |
| 處置防護 | 需依細胞毒性藥物處置規範操作（含個人防護裝備、溢出處理程序） |

具體毒性數據（如骨髓抑制發生率）請參考原廠仿單的警語與注意事項，本評估之相關安全性欄位存在資料缺口。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有多個 Phase 2 單臂試驗直接測試 Vinorelbine（單獨或併用 Cyclophosphamide）於復發/難治性肉瘤族群，其中明確涵蓋尤文氏肉瘤適應症，證據等級達 L2；但現有試驗多為小樣本、非隨機對照設計，且藥物尚未在香港上市，需在防護措施下謹慎推進。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（目前為 Blocking 等級缺口，無法完成 S1 安全性初評）
- 補齊詳細作用機轉 (MOA) 資料，以強化機轉關聯性分析
- 因藥物目前未在香港上市，需評估上市申請或特殊使用管道
- 建議設計前瞻性隨機對照試驗，以驗證 Vinorelbine 於尤文氏肉瘤之獨立療效（現有證據多為單臂試驗或混合肉瘤族群研究）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

