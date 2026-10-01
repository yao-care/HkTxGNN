---
layout: default
title: Tenoxicam
parent: 高證據等級 (L1-L2)
nav_order: 845
evidence_level: L2
indication_count: 5
---

# Tenoxicam
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

# Tenoxicam：從一般 NSAID 用途到類風濕性關節炎

## 一句話總結

Tenoxicam 是 oxicam 類非類固醇消炎止痛藥（NSAID），本次資料未登載明確的原適應症。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
目前有 **1 個臨床試驗登記**（與 RA 無直接關聯）和 **20 篇文獻**，其中多篇為 RA 的雙盲比較試驗。
Tenoxicam 在風濕疾病的使用歷史很長，這更像是既有用途的確認，而不是全新的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未登載適應症文字） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Tenoxicam 屬於 oxicam 類 NSAID，透過抑制 COX-1/COX-2 來減少前列腺素介導的發炎與疼痛。
DrugBank 的作用機轉欄位目前缺資料，上述機轉說明來自預測流程的推論。

發炎與疼痛是類風濕性關節炎的核心症狀，所以機轉上相當吻合。
文獻也顯示，口服、直腸與注射劑型的 tenoxicam 都用於症狀治療，涵蓋類風濕性關節炎、骨關節炎、僵直性脊椎炎等風濕疾病。
Tenoxicam 在這些疾病中療效至少與其他 NSAID 相當。

要注意的是，這個適應症很可能本來就是既有的標示用途，需要和香港 Department of Health 的核准適應症核對。
NSAID 只能緩解症狀，不能改變疾病進程，這點在評估時要區分清楚。

TxGNN 的其他預測中，只有**頭痛疾患 (Headache Disorder)** 有一定支持：一個 Phase 4 試驗正在比較靜脈注射 tenoxicam 與 ibuprofen 治療急性偏頭痛，尚無結果。
**骨關節炎易感性**需先改定義為「症狀性骨關節炎」再評估。
**短指併指症候群**與**眼缺損小眼畸形-肢根型發育不良症候群**沒有合理機轉，可能是知識圖譜的假象，建議暫緩。

## 臨床試驗證據

目前沒有直接針對 RA 的試驗登記。下表是此預測項下唯一的登記試驗，但它研究的是術後疼痛，並非 RA。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | N/A | 完成 | 80 | 比較 tenoxicam、paracetamol 及兩者合併用於雙顎手術後疼痛；未見 RA 族群，對 RA 無直接證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT（雙盲） | Clin Rheumatol | 292 位 RA 患者，比較 aceclofenac 與 tenoxicam 三個月，兩組臨床指標均有改善 |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | 比較性臨床研究（可能為 RCT） | J Rheumatol | 102 位 RA 患者，tenoxicam 20 mg 與 piroxicam 20 mg 療效無差異，不良反應發生率相近 |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | RCT（雙盲） | Br J Clin Pract | 1,328 位骨關節炎或 RA 患者，tenoxicam 與 piroxicam 均改善疼痛與僵硬，RA 組僵硬改善最明顯 |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | 臨床試驗（雙盲） | Eur J Rheumatol Inflamm | 骨關節炎、RA、僵直性脊椎炎；每日一次 20 mg，療效至少與 piroxicam 相當 |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | tenoxicam 對 RA、骨關節炎等風濕疾病為有效的止痛消炎藥，療效至少與其他 NSAID 相當 |
| [3317800](https://pubmed.ncbi.nlm.nih.gov/3317800/) | 1987 | Review | Scand J Rheumatol Suppl | 彙整 133 項臨床研究，雙盲比較顯示療效，最適劑量為 20 mg |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | 多中心臨床研究 | J Int Med Res | 一般診所 2,963 位骨關節炎或 RA 患者，每日 20 mg 連續使用 12 週，並有長期延伸追蹤 |
| [2512637](https://pubmed.ncbi.nlm.nih.gov/2512637/) | 1989 | 長期臨床試驗 | Scand J Rheumatol Suppl | 20 位 RA 患者，合併基礎療法使用四年，初期雙盲比較 tenoxicam 與 piroxicam，兩者均有顯著改善 |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | 開放性研究 | Eur J Rheumatol Inflamm | 79 位關節病變或 RA 患者，使用栓劑每日 20 mg 共 6 週 |
| [41419140](https://pubmed.ncbi.nlm.nih.gov/41419140/) | 2026 | 前臨床製劑研究 | Eur J Pharm Sci | baricitinib 與 tenoxicam 共載之奈米海綿外用凝膠，供 RA 局部治療 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41325 | XOTILON TAB 20MG | PERFECT GROUPS LTD |
| HK-45225 | TENOX TAB 20MG | DELTAPHARM LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢未找到資料。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有多篇 RA 雙盲比較研究（對照 piroxicam、aceclofenac）支持 tenoxicam 的症狀療效，機轉也直接吻合。
但這些研究多為 1980–1990 年代的發表，沒有已登記的 Phase 2/3 試驗，且香港仿單的安全性資料尚未取得。

**若要推進需要：**
- 取得香港 Department of Health 的仿單，確認核准適應症、警語與禁忌症
- 確認 RA 是否已是香港的核准適應症，以判斷這屬於既有用途或新增適應症
- 補充 DrugBank 的作用機轉資料
- 完成安全性篩檢（目前為阻擋項）
- 將「骨關節炎易感性」重新定義為症狀性骨關節炎後再評估
- 持續追蹤 NCT06786650（偏頭痛 Phase 4 試驗）的結果

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

