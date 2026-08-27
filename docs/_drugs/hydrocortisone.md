---
layout: default
title: Hydrocortisone
parent: 高證據等級 (L1-L2)
nav_order: 376
evidence_level: L1
indication_count: 5
---

# Hydrocortisone
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

# Hydrocortisone：從腎上腺皮質功能不全到圓形禿

## 一句話總結

Hydrocortisone 是一種糖皮質類固醇（corticosteroid），傳統上用於治療腎上腺皮質功能不全及各類發炎性/過敏性疾病。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效，
目前有 **4 個相關臨床試驗**支持這個方向，其中包含一項直接以 Hydrocortisone 1% 乳膏對比 Clobetasol Propionate 治療兒童圓形禿的 Phase 3 試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未上市，無許可證登記；依藥理學分類，Hydrocortisone 傳統用於腎上腺皮質功能不全與發炎性疾病） |
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 詳細的作用機轉資料（列為 High severity 資料缺口 DG002）。根據藥理學一般知識，Hydrocortisone 屬於皮質類固醇（corticosteroid），主要透過抑制發炎反應與免疫細胞浸潤發揮療效。

圓形禿 (Alopecia Areata) 為 T 細胞介導的自體免疫性毛囊攻擊，破壞毛囊原有的免疫豁免狀態。Hydrocortisone 作為皮質類固醇，可抑制局部發炎與免疫細胞浸潤，這正是皮質類固醇治療圓形禿的既有藥理基礎——事實上，局部或病灶內注射皮質類固醇本身就是圓形禿的標準治療選項之一。

Hydrocortisone 1% 屬於低效價（low-potency）製劑，臨床上常用於兒童或臉部等敏感部位，以降低皮膚萎縮等副作用風險，但相對於高效價製劑（如 clobetasol）療效較弱。這也解釋了為何現有頭對頭試驗（NCT01453686）將兩者放在一起比較。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 已完成 | 41 | Hydrocortisone 1% 乳膏對比 Clobetasol Propionate 0.05% 乳膏治療兒童圓形禿，為本適應症**唯一直接藥物層級證據**，是 L1 判定的主要依據 |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | 已完成 | 18 | 探討病灶內注射 Triamcinolone acetonide（同類皮質類固醇，非 hydrocortisone 本體）對腎上腺功能（HPA 軸）之影響，提供同藥物類別安全性佐證 |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | NA | 尚未招募 | 72 | 四臂劑量反應試驗，評估落髮/雄性禿治療產品之安全性與療效，設計上與局部皮質類固醇治療相關，但尚無結果可評估 |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | NA | 已完成 | 380 | 探討異常類固醇代謝體對骨密度、骨強度與骨重塑之影響，屬全身性皮質類固醇長期使用安全性研究，非圓形禿療效試驗 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

目前於香港無許可證登記（未上市，`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 註：TFDA 仿單警語與禁忌資料目前缺失（資料缺口 DG001，Severity: Blocking），此項缺口將導致**無法進入 S1 安全性初評**，屬推進此候選藥物前必須優先補齊的項目。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 圓形禿候選有一項 Phase 3、已完成的頭對頭試驗（NCT01453686）直接比較 Hydrocortisone 1% 與 Clobetasol Propionate 治療效果，加上明確的皮質類固醇免疫抑制機轉支持，證據等級達 L1。
- 但目前完全缺乏 TFDA 仿單警語/禁忌與詳細 MOA 資料，安全性初評（S1）尚無法進行，須加上防護措施（Guardrails）後才能推進。

**若要推進需要：**
- **[Blocking]** 取得 TFDA（或其他權責藥政機關）仿單警語與禁忌資料（DG001），以完成 S1 安全性初評
- **[High]** 補齊 DrugBank 詳細作用機轉（MOA）資料（DG002），強化機轉關聯性分析
- 確認香港（或其他目標市場）是否有上市計畫，目前 total_licenses = 0，屬完全未上市狀態
- 因無藥物交互作用（DDI）查詢結果（`query_status: not_found`），建議重新執行 DDI 資料庫查詢

---

### 其他候選適應症（優先順序較低，僅供參考）

TxGNN 對 Hydrocortisone 同時預測了其他掉髮相關適應症，但證據強度明顯較弱，目前建議維持 Hold：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 2 | Alopecia mucinosa | 99.97% | L4 | Hold（現有文獻僅為 cyclosporine 治療案例報告，未使用 hydrocortisone） |
| 3 | Telogen effluvium | 99.97% | L5 | Hold（機轉關聯薄弱，唯一文獻與掉髮病理機轉無直接對應） |
| 4 | Quinquaud's folliculitis decalvans (毛囊炎性禿髮) | 99.97% | L5 | Hold（完全無臨床試驗或文獻佐證，僅為模型純預測） |
| 5 | Alopecia antibody deficiency | 99.96% | L4 | Hold（現有文獻多為自體免疫多腺體症候群案例報告，Hydrocortisone 用於治療伴隨的腎上腺功能不全，而非直接治療掉髮本身） |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

