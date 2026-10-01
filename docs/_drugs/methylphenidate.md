---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 4
---

# Methylphenidate
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

# Methylphenidate：從注意力不足過動症 (ADHD) 到顏指趾生殖器症候群

## 一句話總結

Methylphenidate（哌甲酯）是中樞神經興奮劑，臨床上主要用於 ADHD。
TxGNN 模型預測它可能對**顏指趾生殖器症候群 (Faciodigitogenital Syndrome)** 有效，預測分數極高。
但目前**沒有任何臨床試驗或文獻**支持這個預測，屬於純模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症；依證據包內容為 ADHD |
| 預測新適應症 | 顏指趾生殖器症候群 (Faciodigitogenital Syndrome) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。就已知資訊，Methylphenidate 會抑制多巴胺轉運體 (DAT) 與正腎上腺素轉運體 (NET)。這會提高前額葉與紋狀體的多巴胺、正腎上腺素濃度，進而改善注意力與執行功能。

這個預測的機轉連結只是推測。顏指趾生殖器症候群是 X 染色體連鎖疾病，部分病人被描述有注意力或行為方面的特徵，Methylphenidate 理論上可能改善這類症狀。但沒有任何資料支持這一點。

**需要特別提醒**：預測分數高達 99.998%，卻完全沒有試驗或文獻佐證，很可能是知識圖譜結構造成的假象（artifact），不宜過度解讀。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症（供參考）

同一藥物還有 3 個預測適應症，證據強度差異很大：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|------|-----------|-----------|---------|------|------|
| 2 | 軟骨黏液樣纖維瘤 (Chondromyxoid Fibroma) | 99.991% | L5 | Hold | 良性骨腫瘤，找不到合理的機轉連結，很可能是圖譜假象 |
| 3 | 特定發展障礙 (Specific Developmental Disorder) | 99.988% | L2 | Research Question | 有 1 個已完成的 Phase 2 隨機、雙盲、安慰劑對照交叉試驗，見下方 |
| 4 | 輕型憂鬱症 (Dysthymic Disorder) | 99.109% | L4 | Hold | 無臨床試驗，僅有精神興奮劑輔助抗憂鬱藥的 1998 年病例系列，及提及共病憂鬱的 ADHD 文獻 |

排名 3 的主要證據：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05185583](https://clinicaltrials.gov/study/NCT05185583) | Phase 2 | 完成 | 18 | 評估 Methylphenidate 對 6–12 歲兒童言語失用症 (apraxia of speech) 語音清晰度的影響，與安慰劑比較 |

此試驗規模小（n=18），且尚未見結果發表。排名 3 檢索到的文獻多數談 ADHD，而 ADHD 是另一個疾病實體，只能算間接證據。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證。許可證資料未列劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68143 | NEUROFIND PROLONGED-RELEASE TABLETS 27MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-68145 | NEUROFIND PROLONGED-RELEASE TABLETS 54MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-68144 | NEUROFIND PROLONGED-RELEASE TABLETS 36MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-65758 | MEDIKINET CR MODIFIED-RELEASE CAPSULES 20MG | HUA TAI PHARMACEUTICALS CO LTD |
| HK-65759 | MEDIKINET CR MODIFIED-RELEASE CAPSULES 30MG | HUA TAI PHARMACEUTICALS CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢也未找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（顏指趾生殖器症候群）只有模型分數，沒有任何試驗或文獻，證據等級 L5，也缺乏可信的機轉連結。
- 若要投入研究資源，排名 3 的特定發展障礙（以言語失用症為例）有一個已完成的 Phase 2 試驗，較值得追蹤。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症（目前為阻擋性資料缺口，無法進入安全性篩選）
- 從 DrugBank 補齊作用機轉資料
- 補齊各許可證的核准適應症與劑型，確認原適應症
- 若聚焦排名 3，取得 NCT05185583 的結果，並釐清「特定發展障礙」的疾病定義與 ADHD 的界線
- 針對顏指趾生殖器症候群，先做系統性文獻檢索與病例回顧，再考慮任何臨床驗證

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

