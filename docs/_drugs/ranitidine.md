---
layout: default
title: Ranitidine
parent: 中證據等級 (L3-L4)
nav_order: 742
evidence_level: L3
indication_count: 5
---

# Ranitidine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Ranitidine：從原適應症（資料未載明）到活動性消化性潰瘍

## 一句話總結

Ranitidine 是 H2 受體拮抗劑，用於抑制胃酸分泌，但本次資料中沒有載明原適應症。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **1 個臨床試驗**（相關性低）和 **17 篇文獻**，其中多數為 1980–1990 年代的臨床研究與綜述。
這個適應症很可能本來就是已核准的用途，不算真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證與資料來源均未載明 |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Ranitidine 是 H2 受體拮抗劑，透過阻斷胃壁細胞上的組織胺 H2 受體來抑制胃酸分泌。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自藥理類別與文獻描述。

消化性潰瘍的發生與胃酸、胃蛋白酶等攻擊因子壓過黏膜防禦有關。抑制 24 小時或夜間胃酸，與潰瘍癒合高度相關。文獻也顯示，ranitidine 300 mg/日在十二指腸潰瘍的 4 週癒合率可達 91%（1985 年研究）。

TxGNN 給出 99.89% 的高分，很可能反映知識圖譜中既有的藥物與疾病關聯，而非新發現。此外，臨床上 ranitidine 在多國曾因 NDMA 污染疑慮於 2019–2020 年起下架，香港「已上市」的狀態需要再核實。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | 完成 | 320 | 評估他汀類與質子幫浦抑制劑（PPI）對 clopidogrel 抗血小板效果的影響。未測試 ranitidine 治療潰瘍，對本適應症沒有直接的療效證據（相關性評級 C） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klin Wochenschr | 比較夜間給予 rioprostil（前列腺素類似物）與 ranitidine 在十二指腸潰瘍癒合上的效力與作用時間 |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | 多中心隨機雙盲試驗（尚未分類） | Am J Med | famotidine 對比 ranitidine 治療活動性十二指腸潰瘍，19 國共納入 1,031 名內視鏡確診患者 |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | 隨機雙盲試驗（尚未分類） | J Gastroenterol Hepatol | 270 名十二指腸潰瘍患者，比較 omeprazole 10/20 mg 與 ranitidine 150 mg 每日兩次的癒合與復發 |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | 隨機試驗（尚未分類） | Clin Ther | 160 名患者，8 週癒合率 famotidine 94%、ranitidine 80%，並含 6 個月維持治療 |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | Review（資料庫分類） | Scand J Gastroenterol | ranitidine 300 mg/日，4 週癒合率：十二指腸潰瘍 91%、幽門前潰瘍 68%、胃體潰瘍 81%；另含 1 年維持治療 |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | ranitidine 效力為 cimetidine 的 4–10 倍，療效相當、耐受性相似 |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | 討論前列腺素、H2 受體拮抗劑與消化性潰瘍的關係 |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepatogastroenterology | 抑制夜間或 24 小時胃酸與潰瘍癒合相關 |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | 前瞻對照研究 | Hepatogastroenterology | ranitidine 合併 ecabet 與單用 ranitidine 比較，觀察潰瘍復發，與幽門螺旋桿菌（H. pylori）是否根除無關 |
| [18493408](https://pubmed.ncbi.nlm.nih.gov/18493408/) | 1996 | 前瞻研究 | Diagn Ther Endosc | 23 名齋戒期患者，其中 18 名規律服用 ranitidine 150 mg 每日兩次，齋戒前後以內視鏡比較 |

這批文獻多為比較性研究與綜述，且許多 RCT 的分類尚未完成。證據雖多，但年代偏早，且不少文獻是以其他藥物為主角。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41546 | EUROTAC TAB 150MG | 未提供 | 未提供 |
| HK-60962 | STOMACHAL TAB 150MG | 未提供 | 未提供 |
| HK-55824 | RANTIN TAB 150MG | 未提供 | 未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢無結果。香港衛生署仿單的警語與禁忌尚未取得，這是目前的阻斷性資料缺口。

## 結論與下一步

**決策：Hold**

**理由：**
- 本適應症很可能是既有核准用途，不是真正的新用途，證據等級為 L3，且缺少已完成的 Phase 3 RCT。
- 香港仿單的警語與禁忌尚未取得，無法進行 S1 安全性篩選。
- 市場狀態需要核實，因為 ranitidine 曾因 NDMA 污染疑慮在多國下架。

**若要推進需要：**
- 下載並解析香港衛生署仿單，取得核准適應症、警語與禁忌。
- 核實 3 張許可證的實際有效狀態與 NDMA 相關處置。
- 補齊 DrugBank 的作用機轉資料。
- 完成文獻的研究類型與相關性分類，確認是否有已完成的隨機對照試驗。
- 另外 4 個預測適應症（胃空腸吻合口潰瘍、消化性潰瘍穿孔、十二指腸胃反流、十二指腸阻塞）證據均為間接的 L4，目前也建議 Hold。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

