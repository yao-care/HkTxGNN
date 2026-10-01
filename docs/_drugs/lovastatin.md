---
layout: default
title: Lovastatin
parent: 中證據等級 (L3-L4)
nav_order: 534
evidence_level: L3
indication_count: 5
---

# Lovastatin
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

# Lovastatin：從血脂異常（原適應症待確認）到同型接合子家族性高膽固醇血症

## 一句話總結

Lovastatin 是 HMG-CoA 還原酶抑制劑（statin），香港有 2 張上市許可證，但資料中的原適應症欄位為空白。
TxGNN 預測它可能對**同型接合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效。
目前檢索到 3 個相關臨床試驗和 20 篇文獻，但**這 3 個試驗都沒有以 lovastatin 為試驗藥物**，且 1988 年的研究顯示受體陰性患者幾乎無反應。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 同型接合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。Lovastatin 屬於 statin 類，已知透過抑制 HMG-CoA 還原酶來降低肝臟膽固醇合成，並增加肝臟 LDL 受體表現。

HoFH 是 LDL 受體 (LDLR) 兩個對偶基因都有缺陷的遺傳疾病，LDL-C 極高。Lovastatin 的降脂作用依賴 LDL 受體上調，因此**療效取決於患者殘存的受體活性**。

- **受體缺陷型**（仍有部分受體功能）：機轉上可能有效。
- **受體陰性型**：預期反應差。1988 年 3 名 6–9 歲受體陰性 HoFH 兒童使用 lovastatin 2 mg/kg/day，LDL-C 沒有下降。

因此這個預測在機轉上部分成立，但不是對所有 HoFH 患者都適用。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | Alirocumab 用於 8–17 歲 HoFH 兒童，評估第 12 週 LDL-C 變化。未測試 lovastatin |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | Ezetimibe 合併 atorvastatin 或 simvastatin 的 24 個月長期安全性延伸研究。未測試 lovastatin |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | Ezetimibe 加在 atorvastatin 或 simvastatin 上治療 HoFH 的療效與安全性。未測試 lovastatin |

以上試驗只能說明「statin 加其他藥物」是 HoFH 的治療思路，不構成 lovastatin 的直接證據。

## 文獻證據

已依 RCT > 臨床研究 / 回顧 > 個案報告排序。多數文獻在資料中尚未完成分類，類型依摘要判斷。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT | Circulation | 50 名 HoFH 患者在 atorvastatin 或 simvastatin 基礎上加 ezetimibe，多中心雙盲。非 lovastatin |
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | 臨床研究 | J Pediatr | 3 名受體陰性 HoFH 兒童使用 lovastatin，LDL-C 未下降，LDL 週轉也無改變 |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | 臨床研究 | An Esp Pediatr | 2 名 HoFH 患者使用 lovastatin 合併 probucol 與 cholestyramine，並分析 LDL 受體與療效的關係 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | 回顧兒童與青少年血脂異常的藥物與手術治療，多數經驗來自家族性高膽固醇血症，包含 lovastatin |
| [2643427](https://pubmed.ncbi.nlm.nih.gov/2643427/) | 1989 | Review | Arteriosclerosis | 門腔靜脈分流術與肝臟移植用於嚴重家族性高膽固醇血症 |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe 藥物回顧，說明其作用機轉與 LDL-C 降幅 |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | 個案報告 | JAMA | HoFH 兒童肝臟移植後，LDL 受體活性恢復到約 60%，加用 lovastatin 後膽固醇降至正常 |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | 個案報告 | An Esp Pediatr | 受體缺陷型 HoFH 患者使用 cholestyramine 合併 lovastatin 的反應 |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | 個案報告 | Eur J Pediatr | 7 歲 HoFH 女孩接受 LDL 血漿分離術，並比較加或不加 lovastatin 的效果 |
| [12091863](https://pubmed.ncbi.nlm.nih.gov/12091863/) | 2002 | 個案報告 | J Pediatr | 1 名 HoFH 患者以 H.E.L.P. 血液透析合併 statin 治療 15 年，LDL-C 較基線下降 85% |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 | 規格 |
|---------|------|------|------|
| HK-61102 | OVASTAR TAB 20MG | LSB (HK) LIMITED | 錠劑 20 mg |
| HK-39329 | MEDOSTATIN TAB 20MG | STAR MEDICAL SUPPLIES LTD | 錠劑 20 mg |

目前取得的許可證資料未附核准適應症文字，需查閱香港衛生署核准內容。

## 安全性考量

- **藥物交互作用**：資料庫查詢未找到記錄，不代表沒有交互作用。
- **文獻提示**：資料中有 1988 年 *Ann Intern Med* 的報告（PMID 3421570），標題為 lovastatin 與 nicotinic acid 合併使用和橫紋肌溶解。合併用藥時需特別留意肌肉相關風險。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 3 個 HoFH 試驗都不是 lovastatin 試驗，直接證據只有小規模、年代久遠的研究和個案報告，其中還有一篇顯示受體陰性患者無效。
- 香港仿單的警語與禁忌症資料缺口屬 Blocking，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症。
- 補齊 DrugBank 作用機轉資料。
- 依 LDLR 基因型（受體缺陷型 / 受體陰性型）分層，蒐集 lovastatin 的直接療效證據。
- 與現行 HoFH 標準治療（如 atorvastatin、simvastatin 加其他藥物）比較，確認 lovastatin 是否有臨床價值。

**其他預測適應症（供參考）：**
- 高脂蛋白血症與家族性高膽固醇血症：有較直接的 lovastatin 研究，證據等級 L2，可 Proceed with Guardrails。這兩項與 lovastatin 既有的降脂用途接近，需先確認是否已在核准範圍內。
- 膽固醇 7α-羥化酶缺乏症與膽固醇酯轉運蛋白缺乏症：幾乎無證據，建議 Hold。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

