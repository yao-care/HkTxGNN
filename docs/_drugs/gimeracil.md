---
layout: default
title: Gimeracil
parent: 高證據等級 (L1-L2)
nav_order: 406
evidence_level: L1
indication_count: 5
---

# Gimeracil
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Gimeracil：從 S-1 複方成分到大腸腫瘤

## 一句話總結

Gimeracil 是 S-1 複方（tegafur + gimeracil + oteracil）的成分之一，本身是 DPD 酶抑制劑。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **8 個臨床試驗**支持這個方向（含 2 個已完成的 Phase 3 RCT），但**無相關文獻**。
所有證據都來自 S-1 固定複方，並非 gimeracil 單獨使用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Gimeracil 是可逆性的 dihydropyrimidine dehydrogenase (DPD) 抑制劑，本身不具細胞毒性。
在 S-1 複方中，它減緩 5-FU 的分解，讓體內 5-FU 濃度升高且維持更久。這是 S-1 對大腸直腸癌有效的藥理基礎。

目前缺乏 DrugBank 的詳細作用機轉資料，原適應症欄位也沒有資料。
不過臨床試驗登記顯示，含 gimeracil 的 S-1 已被廣泛用於大腸癌的輔助治療與轉移性治療，
包括與 capecitabine 的直接比較，以及與 oxaliplatin、bevacizumab 等藥物的組合。
這些都支持 TxGNN 的預測，最佳解讀是「gimeracil 作為 S-1 的一部分」。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+Leucovorin 對比 S-1（TS-1），用於 Stage III 結腸癌輔助治療。直接在目標疾病測試含 gimeracil 的療程，為本組最強證據 |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 完成 | 161 | S-1 對比 capecitabine，用於轉移性結直腸癌第一線治療（SALTO 試驗）。屬直接比較，但樣本數小 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX（oxaliplatin + S-1）對比 XELOX，用於 Stage III 結直腸癌輔助化療。規模大且高度相關，但無結果資料 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 未知 | 82 | Raltitrexed 併用 S-1，用於標準化療失敗的轉移性結直腸癌，主要終點為無惡化存活期 |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | 未知 | 42 | S-1、口服 leucovorin 與 oxaliplatin 併用（SOL），用於未經治療的轉移性結直腸癌，支持可行性與劑量 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 未知 | 40 | S-1 併用 bevacizumab，用於先前化療失敗的無法切除或復發性結直腸癌 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib 併用 tegafur/gimeracil/oteracil，用於晚期轉移性結直腸癌第三線治療，僅代表持續有研究興趣 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 已終止 | 20 | 比較 S-1 與 capecitabine（併用 oxaliplatin）對冠狀動脈血流的影響。終點為心血管安全性，非療效 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-61181 | TS-ONE 25 CAP | DKSH HONG KONG LIMITED |
| HK-61182 | TS-ONE 20 CAP | DKSH HONG KONG LIMITED |

## 細胞毒性

Gimeracil 本身不具細胞毒性，但它所屬的 S-1 複方含有 fluoropyrimidine（tegafur），以下依 S-1 複方的藥物類別判斷。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類複方；gimeracil 為 DPD 抑制劑） |
| 骨髓抑制風險 | 中度（依藥物類別判斷） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

具體警語請參考原廠仿單。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 2 個已完成的 Phase 3 RCT（NCT00660894、NCT01918852）以及多個 Phase 2/3 試驗支持 S-1 用於結直腸癌，證據等級為 L1。
但證據全部針對 S-1 固定複方，且多項試驗狀態為「未知」、無文獻佐證，因此需附帶限制條件。

**Guardrails：**
- 建議僅適用於 S-1 療程，不適用於 gimeracil 單獨使用。
- 需注意劑量與 DPD 相關毒性。
- Phase 3 試驗以亞洲族群為主，推論到其他族群需謹慎。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（目前為阻斷性資料缺口）。
- 補齊 DrugBank 作用機轉資料。
- 補充相關文獻，特別是 NCT00660894 與 NCT01918852 的發表結果。
- 確認香港 4 張許可證的核准適應症（目前無資料），以判斷大腸直腸癌是否已在標示內。

**其他預測適應症：** 排名 2–5 的預測（盲腸絨毛狀腺瘤、惡性胃顆粒細胞瘤、結腸脂肪瘤、盲腸神經內分泌腫瘤 G1）分數皆約 99.8%，但沒有任何試驗或文獻支持，證據等級 L5，建議 **Hold**。這些分數可能只反映知識圖譜中與大腸癌的鄰近關係。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

