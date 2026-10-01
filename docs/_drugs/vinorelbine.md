---
layout: default
title: Vinorelbine
parent: 僅模型預測 (L5)
nav_order: 923
evidence_level: L5
indication_count: 5
---

# Vinorelbine
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

# Vinorelbine：從非小細胞肺癌與乳癌到尤文氏肉瘤 (Ewing Sarcoma)

## 一句話總結

Vinorelbine 是長春花鹼類（vinca alkaloid）抗腫瘤藥，文獻提到它常用於乳癌與非小細胞肺癌。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing Sarcoma)** 有效，目前有 **4 個臨床試驗**和 **5 篇文獻**支持這個方向，但缺乏針對尤文氏肉瘤的直接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；文獻提及乳癌、非小細胞肺癌 |
| 預測新適應症 | 尤文氏肉瘤 (Ewing Sarcoma) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L3（無 RCT，僅有單臂 Phase 2 與回顧性證據；Pack 原標 L2，依判定規則下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據模型提供的推論，Vinorelbine 是長春花鹼類藥物，會抑制微管聚合並造成有絲分裂停滯。

尤文氏肉瘤是增殖快速的兒童與年輕成人肉瘤，抗有絲分裂藥物在機轉上合理。已有 Phase 2 研究顯示 Vinorelbine 對難治性兒童肉瘤有活性，其中主要是橫紋肌肉瘤。前臨床研究也發現，Vinorelbine 等微管干擾藥物與 PLK1 抑制劑合用，可在尤文氏肉瘤細胞中協同誘導細胞凋亡。

要注意的是，現有臨床資料多為混合型肉瘤，尚無法單獨拆出尤文氏肉瘤的療效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | 未知 | 210 | Vinorelbine + Cyclophosphamide 用於難治或復發腫瘤（含尤文氏瘤）；結果未確認 |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | 完成 | 50 | 單用 Vinorelbine 治療兒童復發或難治惡性腫瘤；提供兒童活性與安全資料，未顯示尤文氏專屬結果 |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | 招募中 | 105 | CAMPFIRE 兒童與年輕成人主協議；可能涵蓋尤文氏肉瘤，但 Vinorelbine 組別未確認 |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | NA | 進行中（不再招募） | 100 | 中國兒童尤文氏肉瘤風險分層治療的前瞻性世代研究；為觀察性，Vinorelbine 角色不明 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 試驗 | Eur J Cancer | Vinorelbine 加持續低劑量 Cyclophosphamide 用於復發或難治兒童與年輕成人實體瘤，耐受性佳，對橫紋肌肉瘤有效 |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 試驗 | Cancer | Vinorelbine 用於曾接受治療的晚期兒童肉瘤，顯示對橫紋肌肉瘤有活性 |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Front Pharmacol | 軟組織肉瘤化療藥物綜述 |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | 前臨床 | Int J Cancer | PLK1 抑制劑與 Vinorelbine 等微管干擾藥物，在尤文氏肉瘤細胞中協同誘導細胞凋亡 |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urol | 腎臟骨外尤文氏肉瘤病例與文獻回顧，與 Vinorelbine 無直接關聯 |

## 香港上市資訊

香港共有 6 張許可證，以下列出 5 張。Pack 中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67132 | VINORELBINE ALVOGEN CAPSULES 20MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-67133 | VINORELBINE ALVOGEN CAPSULES 30MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-60311 | VINORELBIN EBEWE CONC FOR SOLN FOR INF 10MG/ML | SANDOZ HONG KONG LIMITED |
| HK-60888 | VINORELBINE TARTRATE INJECTION 10MG/ML (QILU HAINAN) | JINDUN PHARMA (H.K.) LIMITED |
| HK-56213 | NAVELBINE CAP 30MG | PIERRE FABRE DERMO-COSMETIQUE HONG-KONG LIMITED |

## 細胞毒性

以下為依藥物類別（長春花鹼類）判斷的一般資訊，Pack 本身無毒性資料，細節請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（長春花鹼類，微管抑制劑） |
| 骨髓抑制風險 | 高（嗜中性白血球減少為常見的劑量限制毒性） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；注射劑型需注意外滲風險 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有單臂 Phase 2 研究與前臨床資料，且主要針對混合型兒童肉瘤或橫紋肌肉瘤，沒有尤文氏肉瘤專屬的療效證據。
- 香港仿單的警語與禁忌資料缺漏（Pack 標為阻斷性資料缺口），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 查詢 DrugBank，補齊作用機轉資料。
- 確認 NCT00180947 與 NCT00003234 中尤文氏肉瘤亞群的療效結果。
- 確認 CAMPFIRE（NCT05999994）是否有 Vinorelbine 組別。
- 兒童與年輕族群的劑量與血液毒性監測計畫。

另有 4 個預測適應症（牙齦纖維瘤、肺纖維瘤、肺溝瘤、肺生殖細胞瘤），證據等級為 L4–L5，均建議 Hold。其中牙齦纖維瘤與肺纖維瘤為良性病變，僅有模型預測，無試驗或文獻支持。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

