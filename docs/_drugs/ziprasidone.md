---
layout: default
title: Ziprasidone
parent: 僅模型預測 (L5)
nav_order: 941
evidence_level: L5
indication_count: 10
---

# Ziprasidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ziprasidone：從精神分裂症與雙相情緒障礙到拔毛症

## 一句話總結

Ziprasidone 是非典型抗精神病藥，臨床上用於精神分裂症與雙相情緒障礙的躁期治療。
TxGNN 模型預測它可能對**拔毛症 (Trichotillomania)** 有效，但目前**沒有任何臨床試驗或文獻**支持，只有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 拔毛症 (Trichotillomania) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

香港許可證資料中沒有核准適應症文字，因此原適應症欄位省略。上述原適應症是依文獻內容判斷。

## 為什麼這個預測合理？

Ziprasidone 是 D2 和 5-HT2A 受體拮抗劑。拔毛症屬於強迫症譜系疾病，與多巴胺和血清素系統的異常有關。這個受體作用特性與拔毛症的病理有合理的關聯。

不過目前沒有檢索到任何針對拔毛症的臨床試驗或文獻。0.998 的高分只代表模型預測，不能視為療效證據。原作用機轉欄位在證據包中缺資料，上述機轉說明來自預測推論，而非 DrugBank 完整 MOA 資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63939 | ZIPRASIDON STADA CAPSULES 40MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-63937 | ZIPRASIDON STADA CAPSULES 60MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-64115 | ZYPSILA CAPSULES 20MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-63940 | ZIPRASIDON STADA CAPSULES 20MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-48925 | ZELDOX CAP 80MG | VIATRIS HEALTHCARE HONG KONG LIMITED |

此處僅列出 12 張許可證中的 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。證據包沒有取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也無結果。

## 同一藥物的其他預測（補充）

證據包共有 10 個預測，排名第 1 的拔毛症證據最弱，其他預測的證據差異很大：

- **重大情感障礙 (Major affective disorder，排名 3，分數 99.66%)**：證據等級 L1。有多項已完成的 Phase 3 隨機對照試驗，例如 NCT00282464、NCT00141271（雙相 I 型憂鬱）和 NCT00312494（急性躁症併用鋰鹽或 divalproex）。另有 Phase 2 試驗（NCT00555997）及多篇系統性回顧。這部分接近原適應症，決策為 Proceed with Guardrails。
- **妥瑞氏症 (Tourette syndrome，排名 7，分數 99.63%)**：證據等級 L3。有一項兒童與青少年先導研究（PMID 10714048）和多篇回顧，決策為 Research Question。主要顧慮是 QT 間期延長，在兒童和青少年中需特別注意。
- **其餘 7 個預測**：包括水腦症、近視相關疾病等，缺乏可信的機轉連結，很可能是知識圖譜的假關聯。

## 結論與下一步

**決策：Hold**

**理由：**
拔毛症預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。機轉上雖有合理性，但不足以推進。

**若要推進需要：**
- 針對拔毛症與 ziprasidone 做專項文獻檢索，包括病例報告
- 取得完整的作用機轉資料（DrugBank）
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症
- 若有意推進，建議優先評估重大情感障礙（排名 3）和妥瑞氏症（排名 7）

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

